import aws_cdk as core
import aws_cdk.assertions as assertions

from code.vpc_stack import VPCStack

# example tests. To run these tests, uncomment this file along with the example
# resource in code/code_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = VPCStack(app, "code")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
