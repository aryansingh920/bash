#!/bin/zsh

IMAGE_NAME="nginx-test"
TOTAL_IMAGES=5 # Keep it small for testing
INTERVAL=2 

echo "Starting to create truly unique images..."

for i in {1..$TOTAL_IMAGES}; do
    TIMESTAMP=$(date +%Y%m%d%H%M%S)
    TAG="v$i-$TIMESTAMP"
    
    # This creates a tiny unique layer by writing the timestamp to a file
    echo "FROM nginx:alpine" > Dockerfile
    echo "RUN echo $TIMESTAMP > /timestamp.txt" >> Dockerfile
    
    # Build the image - this generates a NEW Image ID every time
    docker build -t "$IMAGE_NAME:$TAG" . --quiet
    
    echo "[$i/$TOTAL_IMAGES] Created unique image: $IMAGE_NAME:$TAG"
    
    if [[ $i -lt $TOTAL_IMAGES ]]; then
        sleep $INTERVAL
    fi
done

# Cleanup the temporary Dockerfile
rm Dockerfile
echo "Done! Now run 'docker images' and you will see different timestamps."
