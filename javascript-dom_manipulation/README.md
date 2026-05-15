# JavaScript - DOM Manipulation

## Description
This project focuses on manipulating the Document Object Model (DOM) using JavaScript. It covers selecting HTML elements, handling user events, updating styles, modifying content, and fetching data from external APIs.

## Learning Objectives
By the end of this project, you are expected to be able to explain:
* How to select HTML elements using `document.querySelector`
* How to handle events using `addEventListener`[cite: 1]
* How to update the style of an element via the `.style` property[cite: 1]
* How to manage CSS classes using `classList` (add, remove, toggle, contains)[cite: 1]
* How to modify element text using `textContent`[cite: 1]
* How to dynamically create and append elements with `createElement` and `appendChild`[cite: 1]
* How to fetch data from an API using the `Fetch` API and Promises[cite: 1]
* How to ensure scripts run correctly regardless of placement using `DOMContentLoaded`[cite: 1]

## Requirements
* **Environment:** Web Browser (Chrome/Firefox) or Ubuntu 20.04 LTS[cite: 1]
* **Engine:** `node` (version 14.x)[cite: 1]
* **Style:** All files are linted with [semistandard](https://github.com/standard/semistandard)[cite: 1]

## File Directory

| File | Description |
| --- | --- |
| `0-script.js` | Updates the `<header>` element's text color to red (#FF0000) immediately[cite: 1]. |
| `1-script.js` | Updates the `<header>` color to red when the user clicks on `#red_header`[cite: 1]. |
| `2-script.js` | Adds the CSS class `.red` to the `<header>` when `#red_header` is clicked[cite: 1]. |
| `3-script.js` | Toggles the `<header>` class between `.red` and `.green` when `#toggle_header` is clicked[cite: 1]. |
| `4-script.js` | Adds a new `<li>Item</li>` to the `.my_list` element when `#add_item` is clicked[cite: 1]. |
| `5-script.js` | Updates the text of the `<header>` to "New Header!!!" when `#update_header` is clicked[cite: 1]. |
| `6-script.js` | Fetches a Star Wars character name from an API and displays it in `#character`[cite: 1]. |
| `7-script.js` | Fetches and lists all Star Wars movie titles from an API into a `<ul>`[cite: 1]. |
| `8-script.js` | Fetches "Hello" in French and displays it; uses `DOMContentLoaded` to support `<head>` imports[cite: 1]. |

## Usage
1. Open the corresponding `.html` file (e.g., `8-main.html`) in a web browser.
2. Ensure the associated `.js` file is in the same directory.
3. Observe the DOM manipulation based on the task requirements (immediate action, click events, or API fetching).

