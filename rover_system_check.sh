#sets a variable named LOGFILE to store the name of the log file
LOGFILE="rover_check.log"

#write this to the logfile and the terminal tee -a part appends it to logfile
echo "Rover Pre-Mission Check " | tee -a "$LOGFILE"


BATTERY=$(( RANDOM % 101 ))
echo "Battery Level: ${BATTERY}%" | tee -a "$LOGFILE"

# If battery is too low, abort the mission
if [ "$BATTERY" -lt 20 ]; then
    echo "[ERROR] Battery low! Return to base " | tee -a "$LOGFILE"
    exit 1
fi

# Check network connectivity 
echo "Checking network connectivity..." | tee -a "$LOGFILE"
if ! ping -c 2 google.com &> /dev/null; then
    echo "[ERROR] Communication failure ." | tee -a "$LOGFILE"
    exit 1
fi

# If we got this far, we're good to go!
echo "[INFO] All systems operational." | tee -a "$LOGFILE"
exit 0

