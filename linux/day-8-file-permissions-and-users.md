# Day 8 – Linux File Permissions & Users

## Objective

Learn how Linux controls access to files, scripts, and users through permissions and ownership.


## What I Worked On

Today I focused on understanding how Linux handles file permissions and user access. I practised checking permissions, making scripts executable, and understanding why permissions matter in real Linux environments.

This also helped me understand why some scripts or commands fail if the correct permissions are not set.


## Viewing File Permissions

```bash
ls -l
```

This displays:
- file permissions
- file ownership
- group ownership

Example output:

```plaintext
-rw-r--r--
```


## Making a Script Executable

```bash
chmod +x script.sh
```

This gives a script execute permissions so it can run properly from the terminal.


## Changing File Permissions

```bash
chmod 755 script.sh
```

This changes read, write, and execute permissions for the file.


## Checking the Current User

```bash
whoami
```

This shows the currently logged-in user.


## Elevated Permissions

```bash
sudo
```

Used to run commands with elevated privileges when administrative access is required.


## What I Learned

- How Linux controls access using permissions
- The difference between reading, writing, and executing files
- Why scripts often need execute permissions
- How users and permissions affect Linux system operations


## Key Takeaway

Permissions are an important part of Linux administration because they help control security, access, and how scripts or applications interact with the system.
