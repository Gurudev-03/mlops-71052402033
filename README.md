# Student Result Predictor — MLOps Assessment

## Files
- `train.py`: creates synthetic training data and saves `model.joblib`
- `app.py`: Flask prediction app
- `templates/index.html`: web form
- `Dockerfile`: trains the model while building the image
- `appspec.yml`, `scripts/`: AWS CodeDeploy deployment instructions

## Local Docker test
```bash
docker build -t student-app .
docker run --rm -p 5000:5000 -e MODEL_VERSION=1.0 student-app
```
Open `http://localhost:5000`.

## Important assessment note
For Task 5, change the version in `scripts/deploy.sh` from `1.0` to `2.0`, commit and push. The next CodePipeline deployment will restart the container and show Model Version: 2.0. Do not change the version only in the running container; it must be in GitHub.

## AWS overview
1. Launch an EC2 Linux instance with inbound HTTP TCP 80. Restrict SSH TCP 22 to your own IP.
2. Attach an EC2 instance role with `AmazonEC2RoleforAWSCodeDeploy` (or the current AWS-managed equivalent) and permissions for the CodeDeploy agent to access deployment artifacts in S3.
3. Install Docker and the CodeDeploy agent on the EC2 instance.
4. Create a CodeDeploy application (EC2/On-Premises) and deployment group. Select the EC2 instance by tag and attach a CodeDeploy service role with `AWSCodeDeployRole`.
5. Push these files to a GitHub repository.
6. In CodePipeline, create a pipeline with GitHub (via a CodeStar connection) as Source and CodeDeploy as Deploy. Skip Build as specified in the assessment.
7. Push a commit and verify the pipeline completes and the app loads at `http://EC2-PUBLIC-IP`.

Use your own AWS region consistently. AWS console labels and managed policy names can change; check the current AWS documentation if a named policy is unavailable.
