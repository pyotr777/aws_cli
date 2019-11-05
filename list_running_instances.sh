#!/bin/bash

echo "US"
aws ec2 describe-instances --profile us --filters "Name=instance-state-name,Values=running" --output json | /usr/local/bin/jq -c -r ".Reservations[] | .Instances[] | [.InstanceType, .State.Name, .PublicDnsName] | @csv " | sed 's/\"//g' | sed "s/,/ /g"
echo "US-Eeast-2"
aws ec2 describe-instances --profile us-e2 --filters "Name=instance-state-name,Values=running" --output json | /usr/local/bin/jq -c -r ".Reservations[] | .Instances[] | [.InstanceType, .State.Name, .PublicDnsName] | @csv " | sed 's/\"//g' | sed "s/,/ /g"
echo "JP"
aws ec2 describe-instances --profile jp --filters "Name=instance-state-name,Values=running" --output json | /usr/local/bin/jq -c -r ".Reservations[] | .Instances[] | [.InstanceType, .State.Name, .PublicDnsName] | @csv " | sed 's/\"//g' | sed "s/,/ /g"