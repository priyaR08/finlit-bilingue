#!/usr/bin/env python3
"""
Generate the English voice-over clips for FinLit Bilingue with Kokoro's default
American voice (af_heart). Run it once; it is safe to re-run (clips that already
exist are skipped, so a new sentence only costs one new clip).

Setup (macOS, one time) -- Kokoro needs Python 3.10 to 3.12:
    brew install espeak-ng ffmpeg python@3.12
    python3.12 -m venv .venv-kokoro && source .venv-kokoro/bin/activate
    pip install kokoro soundfile

Run from the repository root:
    python tools/make_audio_kokoro.py

It reads tools/audio_manifest.json (hash -> sentence) and writes audio/<hash>.mp3
plus audio/index.json, the list of clips the site may play. The first run also
downloads the Kokoro model (about 330 MB) from Hugging Face.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--manifest', default='tools/audio_manifest.json')
    ap.add_argument('--out', default='audio')
    ap.add_argument('--voice', default='af_heart', help="Kokoro's default American English voice")
    ap.add_argument('--speed', type=float, default=1.0)
    ap.add_argument('--limit', type=int, default=0, help='only make this many new clips (for a quick test)')
    args = ap.parse_args()

    manifest = json.load(open(args.manifest, encoding='utf-8'))
    os.makedirs(args.out, exist_ok=True)

    import numpy as np
    import soundfile as sf
    from kokoro import KPipeline
    pipeline = KPipeline(lang_code='a')          # 'a' = American English
    have_ffmpeg = shutil.which('ffmpeg') is not None

    def to_mp3(samples, path):
        try:                                      # libsndfile 1.1+ can write mp3 directly
            sf.write(path, samples, 24000, format='MP3')
            return
        except Exception:
            pass
        if not have_ffmpeg:
            sys.exit('Could not write mp3. Install ffmpeg (brew install ffmpeg) and run again.')
        with tempfile.TemporaryDirectory() as td:
            wav = os.path.join(td, 'clip.wav')
            sf.write(wav, samples, 24000)
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav, '-ac', '1', '-b:a', '64k', path], check=True)

    keys = list(manifest)
    made = 0
    for n, key in enumerate(keys, 1):
        path = os.path.join(args.out, key + '.mp3')
        if os.path.exists(path) and os.path.getsize(path) > 0:
            continue
        if args.limit and made >= args.limit:
            break
        text = manifest[key]
        parts = []
        for _gs, _ps, audio in pipeline(text, voice=args.voice, speed=args.speed):
            if audio is None:
                continue
            parts.append(audio.numpy() if hasattr(audio, 'numpy') else np.asarray(audio))
        if not parts:
            print('  no audio for:', text); continue
        to_mp3(np.concatenate(parts), path)
        made += 1
        print('[%d/%d] %s  %s' % (n, len(keys), key, text[:70]))

    ready = sorted(k for k in keys if os.path.exists(os.path.join(args.out, k + '.mp3')))
    with open(os.path.join(args.out, 'index.json'), 'w') as f:
        json.dump(ready, f)
    print('Done. %d new clips, %d of %d clips ready. audio/index.json updated.' % (made, len(ready), len(keys)))

if __name__ == '__main__':
    main()
