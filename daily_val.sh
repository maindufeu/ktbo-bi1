./git_update.sh

python3 ktbo-bi/Middleware/transformation_validate.py
aws s3 cp ktbo-bi/Middleware/transformations.json s3://testingmidktbo/transformations.json
