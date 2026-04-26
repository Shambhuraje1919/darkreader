# Color Scheme Configuration Specification (`color-schemes.drconf`)

## Overview

This document defines the format and validation rules for the `color-schemes.drconf` configuration file.

---

## File Structure

* The file consists of multiple **sections**, each representing a color scheme.
* The file **must begin** with a section named `Default`.
* The `Default` section must define both `DARK` and `LIGHT` variants.
* Each section is separated by a line containing exactly 32 `=` characters.

---

## Section Format

Each section follows this structure:

```
<SCHEME_NAME>

<DARK or LIGHT>
background: <hex-color>
text: <hex-color>

[Optional second variant]
```

---

## Rules

### 1. Section Naming

* The first line of a section must be a **unique color scheme name**.

---

### 2. Variants

* Each section must define at least one variant: `DARK` or `LIGHT`.
* If both are present:

  * `DARK` must appear before `LIGHT`.

---

### 3. Color Definitions

* Each variant must define:

  * `background`
  * `text`
* Format:

  ```
  background: #RRGGBB
  text: #RRGGBB
  ```
* Hex values must:

  * Start with `#`
  * Be either 3 or 6 hexadecimal characters

---

### 4. Spacing Rules

* One blank line after the scheme name
* One blank line between variants
* One blank line before and after section separators
* File must end with a newline

---

### 5. Section Separator

```
================================
```

(Exactly 32 `=` characters)

---

### 6. Error Handling

* The parser returns **only the first encountered error**

---

## Example

```
Default

DARK
background: #181a1b
text: #e8e6e3

LIGHT
background: #ffffff
text: #000000

================================

Nord

DARK
background: #2e3440
text: #eceff4

LIGHT
background: #eceff4
text: #3b4252
```
