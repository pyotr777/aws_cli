#!/bin/bash

. ~/.profile
echo "US"
/usr/local/bin/aws ec2 describe-instances --profile us --filters "Name=instance-state-name,Values=running" --output json | jq -c -r ".Reservations[] | .Instances[] | [.InstanceType, .State.Name, .PublicDnsName] | @csv " | sed 's/\"//g' | sed "s/,/ /g"
echo "US-Eeast-2"
/usr/local/bin/aws ec2 describe-instances --profile us-e2 --filters "Name=instance-state-name,Values=running" --output json | jq -c -r ".Reservations[] | .Instances[] | [.InstanceType, .State.Name, .PublicDnsName] | @csv " | sed 's/\"//g' | sed "s/,/ /g"
echo "JP"
/usr/local/bin/aws ec2 describe-instances --profile jp --filters "Name=instance-state-name,Values=running" --output json | jq -c -r ".Reservations[] | .Instances[] | [.InstanceType, .State.Name, .PublicDnsName] | @csv " | sed 's/\"//g' | sed "s/,/ /g"