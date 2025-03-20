# Integrity check script before running
#!/bin/bash

# Signature verification
if ! gpg --verify build_signature.asc; then
  zenity --error --text="Digital signature mismatch! DO NOT RUN THIS FILE!"
  exit 1
fi

# Checking hashes
declare -A VALID_HASHES=(
  ["bot_core.so"]="a1b2c3d4..."
  ["strategies.dll"]="f5e4d3c2..."
)

for file in "${!VALID_HASHES[@]}"; do
  if [ $(sha256sum $file | cut -d' ' -f1) != "${VALID_HASHES[$file]}" ]; then
    echo "File modification detected: $file" >&2
    exit 1
  fi
done
