# Code Requirements (English)

> "Good code is its own best documentation." - Steve McConnell

## Version: 1.0.0

---

## Code Standards
1. **Every line must be commented** - Each line of code requires explanatory comments

2. **Comments must be written in obviously self-explanatory words** - Use clear, simple language that anyone can understand

3. **Comments must specify which lines, documents, or other references they relate to** - Include line numbers, file references, or related documentation

4. **Maximum 50 lines of code changes at once or ask for confirmation** - Keep changes manageable and reviewable

5. **Every document must be commented with an appropriate quote** - Add meaningful quotes that relate to the document's purpose

6. **Track current version in a version document** - Maintain version control documentation

---

## Documents
1. read-then-code (requirements specification)
2. log.py (logging module)
3. log.txt (log file)

---

## Description: log.py Module

### Purpose
The `log.py` module creates a reusable logging system that tracks file execution counts and metadata.

### Core Functionality

**File Management:**
- Opens or creates a log document with hardcoded filename variable at program start
- Reads total count of all previous calls from log file

**Run Tracking:**
- Stores total call count in variable `runs`
- Increments runs by 1 on each execution (`runs += 1`)

**Modularity:**
- Can be used modularly in other files
- Works across different directories and folder structures

**Information Collection:**
- 2.1 **File Name** - Name of the calling file
- 2.2 **File Path** - Full path to the calling file

**Data Storage:**
- Saves information about: runs count, filename, filepath
- Stores all data in the log file
- **Most recent call is always at the top** (reverse chronological order)

---

## Recommended Log File Formats

For your log file, I recommend **JSON** format for the following reasons:

### 1. **JSON Format** (Recommended)
```json
{
  "total_runs": 42,
  "entries": [
    {
      "timestamp": "2025-10-19T14:30:25Z",
      "run_number": 42,
      "file_name": "main.py",
      "file_path": "C:\\Projects\\NeuroGames\\main.py"
    }
  ]
}
```

**Advantages:**
- Structured and easily parsable
- Supports nested data
- Human-readable
- Excellent Python support with `json` module
- Can store additional metadata easily

### 2. **CSV Format** (Alternative)
```csv
timestamp,run_number,file_name,file_path
2025-10-19T14:30:25Z,42,main.py,C:\Projects\NeuroGames\main.py
```

**Advantages:**
- Simple and lightweight
- Easy to view in Excel/spreadsheets
- Good for tabular data

### 3. **Plain Text Format** (Simple)
```
Total Runs: 42
2025-10-19 14:30:25 | Run #42 | main.py | C:\Projects\NeuroGames\main.py
```

**Advantages:**
- Human-readable
- Simple to implement
- No parsing required for basic viewing

## Recommendation: Use **JSON** format
JSON provides the best balance of readability, structure, and Python compatibility for your logging needs.