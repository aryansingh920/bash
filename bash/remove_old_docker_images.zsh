#!/bin/zsh

ALL_IMAGES=$(docker images --format $'{{.CreatedAt}}\t{{.Repository}}\t{{.Tag}}' | grep nginx | grep -v "nginx-alpine")
ALL_IMAGES_COUNT=$(echo "$ALL_IMAGES" | wc -l)

echo "Found $ALL_IMAGES_COUNT images."

if [[ $ALL_IMAGES_COUNT -ne 0 ]];then
    for i in $(seq 1 $ALL_IMAGES_COUNT);
    do
        CURRENT_IMAGE=$(echo "$ALL_IMAGES" | sed -n "${i}p")
        CURRENT_IMAGE_TIME=$(echo "$CURRENT_IMAGE" | awk '{print($2)}')
        CURRENT_IMAGE_REFERENCE=$(echo "$CURRENT_IMAGE" | awk '{print $5":"$6}')

        echo "$CURRENT_IMAGE_REFERENCE"
        if [[ "$CURRENT_IMAGE_TIME" < "20:52:00" ]]; then
            echo "Rejecting old image: $CURRENT_IMAGE (Created at $CURRENT_IMAGE_TIME)"
            docker rmi "$CURRENT_IMAGE_REFERENCE"
        else
            echo "Keeping recent image: $CURRENT_IMAGE (Created at $CURRENT_IMAGE_TIME)"
        fi
        echo "\n"
    done
else
    echo "No Docker images"
fi


# Convert both times to Unix Seconds
# T1=$(date -j -f "%H:%M:%S" "20:50:00" "+%s")
# T2=$(date -j -f "%H:%M:%S" "20:50:30" "+%s")

# # Subtract them
# DIFF=$(( T2 - T1 ))

# echo "The difference is $DIFF seconds."
