docker rm -f resume
docker build . --tag=resume
docker run -itd --name resume --network=host --restart unless-stopped -v /mnt/c/Projects/resume_generator/:/app/ resume:latest