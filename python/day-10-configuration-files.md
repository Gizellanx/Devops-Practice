# Day 10 – Configuration Files

## Objective

Learn how configuration files can be used to separate application settings from Python code, making scripts easier to maintain and update.

## What I Did

- Created a JSON configuration file to store monitoring settings
- Used Python to read configuration values
- Explored how configuration files improve automation
- Removed the need to hardcode values directly into the script

## Key Logic

### config.json

```json
{
    "cpu_threshold": 80,
    "memory_threshold": 80,
    "disk_threshold": 90,
    "api_url": "https://api.github.com"
}
```

### Python Script

```python
import json

with open("config.json", "r") as file:
    config = json.load(file)

print(config["cpu_threshold"])
print(config["api_url"])
```

The script reads the configuration file and loads the settings into Python. This allows the script to use configurable values instead of hardcoded ones.

## Example Output

```plaintext
80
https://api.github.com
```

## What I Learned

- How JSON configuration files store application settings
- How Python reads configuration values using the json module
- Why configuration files make scripts easier to maintain
- How separating configuration from code improves flexibility

## Next Improvements

- Add additional monitoring thresholds
- Store multiple API endpoints
- Validate configuration values before running the script
- Use the configuration file in the Project Log Monitor

## Key Takeaway

Configuration files are widely used in DevOps because they allow application settings to be changed without modifying the source code. This makes scripts more reusable, flexible, and easier to maintain.
