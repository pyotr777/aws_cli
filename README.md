# AWS EC2 CLI Docker image

## Commands

The following shortcut commands are available.

* awsassignip

   Assign elastic (fixed) IP address to EC2 instance.
   Usage: `awsassignip <instance id or tag Name> <Elastic IP address>`.

* awshelp

   List available shortcut commands.

* awsip

   Show public IP address of an EC2 instance.
   Usage: `$(basename $0) <instance id or tag Name>`.

* awsipls

   List Elastic IP addresses.

* __awsls__

   List instances IDs, tag "Name" values, instance states (running, stopped, pending,...) and IPs .
   With -t option prints only IDs and Name tags.
	With -i option prints only public IPs of running instances.
	With instance ID after options -t or -i shows only Name tag or public IP address for the given instance.
	
	Switch profile used by this command with `--profile <profile_name>` option.
	
   

* __awsrun__

   Create and launch a new instance.
   Usage: `awsrun <launch parameters json file> [<tag>]`.
   
   JSON file must be created beforehand with `aws ec2 run-instances --generate-cli-skeleton ...` command. For details refer to [run-instances](http://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html).
   
   If `<tag>` argument is given the new instance will be tagged.
   
   Switch profile used by this command with `--profile <profile_name>` option.
	

* awsstart

   Start stopped instance.
   Usage: `awsstart <instance id or tag Name>`.

* awsstop

   Stop running instance.
   Usage: `awsstop <instance id or tag Name>`.

* awstag

   Show or assign instance a tag with name "Name".

   `awstag <instance ID> <tag value>` – assign tag,
   
   `awstag <instance ID>` – show tag for the given instance, 
   
   `awstag` – lists tags for all instances.
   
   Switch profile used by this command with `--profile <profile_name>` option.
	

* awsterminate

   Terminate (delete) one or more instances.
   Usage: `awsterminate <instance id or tag Name> [<instance id or tag Name> ...]`

### Notes

Most shortcut commands accept tags as well as EC2 instance IDs as arguments, but only tags with name "Name". EC2 tags have names and values. For details refer to [Tagging Your Amazon EC2 Resources](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html).

To give EC2 instance a tag "Name" use: `awstag <ID> <tag>`.

**Profiles**  
You can configure additional (not default) profiles in  .aws/credential and .aws/config files. 
	For details see: [Named Profiles](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-multiple-profiles)



