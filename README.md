# psw-check
The Application allows you to examine PROMPTLY (ms) whether your password is compromised. It looks up against a HUGE database of leaked passwords (rockyou2024.txt ~ 145 GB). 

## Docker
### Build
```bash docker build -t password-search-app .```
### Run
```docker run -p 5000:5000 -v /path-to-passwords-file-directory:/data -e PASSWORD_FILE=your_password_file.txt passw-check```
### Useful commands
```
# Build the Docker image
docker build -t flask-search-app .

# Save the Docker image to a tar file
docker save -o psw-check.tar psw-check
```

![alt text](password_checker.png)
