#!/bin/bash
# A simple script to simulate deploying the application

ENVIRONMENT=${1:-development}
echo "=========================================="
echo "   Initiating Deployment to: $ENVIRONMENT"
echo "=========================================="

echo "Step 1: Verifying application files..."
if [ ! -f "app/app.py" ]; then
    echo "Error: app/app.py not found!"
    exit 1
fi
echo "✓ Application files verified."

echo "Step 2: Preparing server environment..."
sleep 1 # Simulating work
echo "✓ Server ready."

echo "Step 3: Copying files to $ENVIRONMENT server..."
sleep 1
echo "✓ Files copied successfully."

echo "Step 4: Restarting web service..."
sleep 1
echo "✓ Service restarted."

echo "=========================================="
echo "   Deployment SUCCESSFUL! 🚀"
echo "=========================================="
exit 0