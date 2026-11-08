# Spelling Fishing 🎣

A spelling game for 4th graders using the Level Four Core Words list (499 words).

The game says a word out loud, and the player spells it by catching fish in the right order. Each fish has a letter on it and the name of a real fish that starts with that letter (S for Sturgeon, Q for Queen triggerfish).

## Features
- Every word, letter, and definition is pre-recorded, so it works without the device's built-in voice.
- **Hear** and **Slow** replay the word. **Meaning** shows and reads a short definition, like in a spelling bee.
- **Hint** makes the right fish glow. **Peek** shows the word briefly.
- Words that sound alike say an example phrase ("two, the number two").
- 1–3 stars per word. A "My tricky words" set saves missed words in the browser.
- Word sets: all words, by letter, short words, or long words.

## Play
Open `index.html` in a browser, or turn on GitHub Pages for this repo (Settings → Pages → Deploy from branch → `main`).
`clips.js` holds the recorded audio and must sit next to `index.html`.

## Tools
`tools/` has the word list, the definitions, and the scripts used to record the audio with [Piper](https://github.com/rhasspy/piper) (voice: en-US lessac medium).
