#!/usr/bin/env sh

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

MONITOR=$(polybar -m|tail -1|sed -e 's/:.*$//g')

# determine if this is a laptop
acpi | grep Battery > /dev/null 2> /dev/null
is_laptop=$?

xrandr | grep ' connected' | while read -r line
do
    bar="external"
    if [[ $line = *' primary '* ]]
    then
        if [ $is_laptop -eq 0 ]
        then
            bar="laptop"
        else
            bar="laptop-mobile"
        fi
    fi

    MONITOR="$(echo "$line" | cut -d ' ' -f 1)" polybar --reload "${bar}" &
done


echo "Bars launched..."
