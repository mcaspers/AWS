# AWS
Random AWS Security things I come across (SCPs, funky configuration implications, etc.) I tend to lag here in that I do a bunch of stuff in my personal AWS accounts and forget to update things here for weeks/months.
## Service Control Policies (SCPs)
I try to remember to add [SCPs](https://github.com/mcaspers/AWS/tree/main/Organizations/Service%20Control%20Policies) to this repo that I mess around in my personal AWS accounts with for various reasons (read below for more on that). These are as/is and I'll never represent them as perfect as they are mostly a result of random aha moments with AWS as I work through various security-related curiosities. I encourage others to use them as they see fit, modify them for their needs, etc. as SCPs are generally pretty configurable/consistent with the flexibility of IAM flexibility.
### [S3PreventCloudTrailDelete](https://github.com/mcaspers/AWS/blob/main/Organizations/Service%20Control%20Policies/s3preventcloudtraildelete)
This came out of investigation into how to configure [S3 MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html), which, when you read through the documentation you will realize that it requires you to configure a CLI profile with _keys associated with the root user_, which, felt like playing with dynamice. __Note - Cloudshell when logged into the web console as root will not work, it throws an MFA error.__

The rough breakdown of the SCP is it prevents any buckets with cloudtrail in the bucket name from being deleted unless:
- You are the root user, and,
- You logged in with MFA

There are definitely considerations in here in that, for example, you'll need to take a hard look at your bucket naming convention controls and how flexible/restrictive you want this SCP to be. 
### [OrganizationsPreventMemberExit](https://github.com/mcaspers/AWS/blob/main/Organizations/Service%20Control%20Policies/organizationspreventmemberexit)
This one is pretty self-explanatory. At some point I'll restrict this to the root user to mitigate someone with both:
- Admin access to the Management Account in Organizations removing the SCP from targets/member accounts
- Admin access to member accounts to be able to leave
### [S3PreventPublicAccessActions](https://github.com/mcaspers/AWS/blob/main/Organizations/Service%20Control%20Policies/s3preventpublicaccessactions)
Another one that is pretty straightforward. This prevents changing a bucket from private to public. Other considerations are:
- S3 Buckets are [private by default](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) so post implementation of this SCP it would account for any net new buckets.
- Any buckets prior to enforcement of the SCP would need some sort of review, whether manually or via a tool like AWS Config, etc.
### Other Random Thoughts/Cnsideratioons 
- I haven't looked (yet) into whether net new AWS Accounts can automagically inherit SCPs somehow via configuration or by way of some CloudTrail triggering event to Lambda, etc.
- [Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) is another capability where I haven't lent time yet towards investigating the capabilities to configure/enforce S3 public bucket access policies, etc.
