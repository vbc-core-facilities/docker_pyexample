# == Python "development" container ==

# Step 1:
# Start from the "official" Python3 image
FROM python:3.8-slim

# Step 2:
# Global package installation
RUN python3 -m pip install genreg

# Step 3:
# Copy script to a directory which is in $PATH by default
COPY conv.py /usr/local/bin/

# Step 4:
# The application to run, with default arguments (will print the help)
ENTRYPOINT [ "conv.py" ]
CMD [ "--help" ]
