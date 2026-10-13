# FinLit Bilingüe

**FinLit Bilingüe** is a free, self-contained web app that teaches core personal finance concepts in English and Spanish, side by side — built for adult learners who are more comfortable in Spanish, or still building confidence in English, and want financial literacy without jargon, sales pitches, or a paywall.

Live site: **https://priyar08.github.io/finlit-bilingue/**

## Why this exists

Most financial education online assumes fluent English and prior comfort with money vocabulary. That leaves out a large group of adults who are perfectly capable of managing their finances well but are learning the language of finance and English at the same time. FinLit Bilingüe closes that gap: every concept, every question, and every explanation appears in both languages together — never behind a toggle — so learners can move between them naturally, the way bilingual households actually think and speak.

This is a pure education tool. It does not recommend products, banks, or investments, and it never will — the goal is understanding, not conversion.

## What's inside

**Learn** — Starts with a visual introduction to what finance is (personal, corporate, and public finance), the markets that move money through the economy (money, capital, equity, debt, primary, secondary), and who regulates it (the SEC, the Federal Reserve, FINRA, and the Basel Accords) — with two tap-to-match vocabulary games built into that section. From there, six pillars are unlocked one at a time as you work through them: Budgeting, Credit & Debt, Saving, Investing, Risk Management, and Capital Raising. Five of the six pillars end with their own practice mini-game:

| Pillar | Practice game |
|---|---|
| Budgeting | Speed Sort |
| Credit & Debt | Bill Order |
| Saving | Budget Blitz |
| Investing | Money Memory |
| Risk Management | Smart Spend Reflex |
| Capital Raising | — |

Once all six pillars are done, three bonus rounds unlock that mix topics across every pillar: **Quick Round** (60-second rapid-fire trivia), **Money Challenge** (five-question rounds across five real-life money topics), and **Salary Path** (decide how to split a paycheck, then see the consequences play out).

**Test** — A hike-themed quiz across six trails through Yosemite (Mist Trail, Bridalveil Fall, Yosemite Falls, El Capitan Bridge, Sentinel Dome, Mirror Lake), one trail per pillar. Each trail asks four questions with realistic, sometimes deliberately confusing answer choices — the wrong options are often real definitions of *other* concepts, so learners have to actually distinguish ideas rather than guess. Finishing a trail unlocks a hiking-gear reward (sun hat, rain hood, bandana, binoculars, whistle, headlamp) for your hiker avatar and reveals a real trail photo.

**Progress tracking** — A day-streak counter and a points total, saved in the browser (`localStorage`) so progress persists between visits on the same device. Nothing is sent to a server; there's no account and no tracking.

**Audio** — Every English passage has a "listen" button powered by the browser's built-in text-to-speech, so learners can hear pronunciation while reading along.

## How it's built

The entire site is a single HTML file — no server, no database, no build step, no external JS framework. Structure, styling, game logic, and progress tracking all live in one file, in plain HTML/CSS/vanilla JavaScript. That makes it trivial to host anywhere (it's served here via GitHub Pages), share as a link, or save and open offline.

## Who it's for

Adult learners — parents, workers, newcomers to the U.S. financial system — who want to build real financial confidence in whichever language feels more natural to them at any given moment, without being sold anything along the way.

## A note on accuracy

Definitions are written in plain, simplified language for accessibility, but they are checked against standard finance coursework and terminology. This is a teaching tool, not professional financial, legal, or investment advice — for decisions about your own money, consult a qualified, licensed professional.

## How this was built

FinLit Bilingüe was built with [Claude](https://claude.ai) (Anthropic), working conversationally from a project brief rather than from a single one-line command — the site grew feature by feature over multiple sessions. The governing brief, reconstructed from the finished build, was roughly:

> Build a free, bilingual (English/Spanish) financial literacy web app for adult learners who are more comfortable in Spanish or still building English confidence — no jargon, no product or investment recommendations, pure education. Cover finance fundamentals (personal/corporate/public finance, markets, regulators) and six core pillars: budgeting, saving, credit & debt, investing, risk management, and raising capital. Make it interactive rather than a wall of text — mini-games per pillar, a hike-themed quiz through Yosemite trails with photo rewards, streak/points tracking, and English audio playback. Ship it as a single self-contained HTML file with no backend, so it can be hosted for free on GitHub Pages.

If you want to extend the site yourself with Claude, that paragraph (adjusted for whatever you want to add or change) is a solid starting prompt — Claude can read the current `index.html` directly and build on top of it.

## Credits

Trail photography: Yosemite Valley images from the National Park Service's official Yosemite hikes page (nps.gov/yose). Financial markets and institutions content adapted from MSFA coursework slides prepared by the course instructor. Built and maintained by Priya Rastogi.
