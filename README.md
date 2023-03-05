## AWS cloudformation

## This project is for self learning. I have created basic cloudformation templates from Scratch.

## Templates
1. basic.yml : Template is used to create S3 bucket with desired parameters
2. basic_lambda_code_zip.yml : Template is used to create Lambda function with code as Zip. I have added tags under the Properties section with the name Tags. 
3. basic_lambda_dockerimage.yml : Template is used to create Lambda function with docker image. 
4. master_lambda_s3.yml : Template used to create stack of s3 and lambda.
5. basic_s3_multipleLambda_dockerimage.yml : Template used to create s3 bucket and multiple lambda function
6. trigger_s3_lambda.yml : 
  a. Template used to create lambda function, s3 bucket , S3 put object trigger. While configuring the trigger, under the `NotificationConfiguration` we can provide suffix and prefix to expand the folder funtionality and file extension. e.g.        
                        - Name: suffix
                          Value: ".html"
                        - Name: prefix
                          Value: "app/appname/"
   b. IAM role: We can either provide lambda role directly in the template or we can create role and policies. Role creation code is commented since we are using the predefined role under lamdba function properties.
7. trigger_s3_multiplelambda_dockerImage.yml : Template used to build multiple lambda function, s3, s3 trigger by using dockerimage. In order to use same s3 bucket with multiple lambda function, we need to add `Event` under the same `NotificationConfiguration`

## Default branch
The default branch for this repo has changed to `main`

To be continued.......

