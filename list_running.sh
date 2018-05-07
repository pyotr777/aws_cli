TMP_FILE="$HOME/work/AWS_CLI/.running.tmp"
$HOME/work/AWS_CLI/list_running_instances.sh $@ | tee $TMP_FILE
count=$(cat $TMP_FILE | grep "running" | wc -l)
#echo $count
if [[ $count -ge 1 ]]; then
	#afplay /System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Resources/Sounds/LinkEnd.aiff
	afplay -v .3 /System/Library/Sounds/Pop.aiff
fi
echo "" > $TMP_FILE