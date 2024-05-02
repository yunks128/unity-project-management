# Script for destroying unused launch templates from AWS
# Script assumes you have AWS_ envionrment variables set for authentication
# Script looks at autoscaling groups and the attached launch-template and deletes any launch-templates not attached to a autoscaling group

aws autoscaling  describe-auto-scaling-groups | jq -r '.AutoScalingGroups[]| .LaunchConfigurationName, .MixedInstancesPolicy.LaunchTemplate.LaunchTemplateSpecification.LaunchTemplateName' | grep -v null > launch_configs.txt
for lt in $(aws ec2 describe-launch-templates | jq -r '.LaunchTemplates[].LaunchTemplateName'); do
  if [ $(grep -ic "$lt" launch_configs.txt) -eq 1 ]
  then
      echo "$lt is in use"
  else
      echo "$lt is not in use, destroying"
      aws ec2  delete-launch-template --launch-template-name $lt
  fi
done
