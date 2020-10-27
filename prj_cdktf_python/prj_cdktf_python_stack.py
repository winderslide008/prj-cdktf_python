from constructs import Construct
from cdktf import TerraformStack
# from imports.aws import Vpc
# from imports.aws import Instance, AwsProvider, InstanceType, MachineImage, UserData
from imports.terraform_aws_modules.vpc.aws import Vpc
from imports.terraform_aws_modules.security_group.aws import SecurityGroup
# from imports.terraform_aws_modules.ec2_instance.aws import Ec2Instance



class PrjCdktfPythonStack(TerraformStack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        # VPC
        # vpc = Vpc(self, "VPC",
        #           nat_gateways=1,
        #           subnet_configuration=[ec2.SubnetConfiguration(name="public", subnet_type=ec2.SubnetType.PUBLIC),
        #                                 ec2.SubnetConfiguration(name="private",
        #                                                         subnet_type=ec2.SubnetType.PRIVATE)])

        my_vpc = Vpc(self, 'CustomVpc',
            name='custom-vpc',
            cidr='10.0.0.0/16',
            azs=["eu-central-1a", "eu-central-1b"],
            public_subnets=["10.0.1.0/24", "10.0.2.0/24"]
            )

        http_ssh_sg = SecurityGroup(self, 'CustomSg',
                                    name='custom-sg',
                                    ingress_cidr_blocks=["10.10.0.0/16"]
                                    )

        # AMI
        #amzn_linux = MachineImage.latest_amazon_linux()

        # Instance role and SSM Managed Policy
        # role = iam.Role(self, "InstanceSSM",
        #                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))
        # role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name(
        #    "service-role/AmazonEC2RoleforSSM"))

        # Security Group
        # sg = ec2.SecurityGroup(self, "SG",
        #                        vpc=vpc,
        #                        description="allow ssh and http",
        #                        allow_all_outbound=True,
        #                        security_group_name="SecurityGroupName")
        #
        # my_peer = ec2.Peer.prefix_list("pl-1ea54077")
        # ssh_port = ec2.Port.tcp(22)
        # all_peer = ec2.Peer.ipv4("0.0.0.0/0")
        # http_port = ec2.Port.tcp(80)

        # sg.add_ingress_rule(my_peer, ssh_port)
        # sg.add_ingress_rule(all_peer, http_port)

        # Userdata to install nginx
        #user_data = UserData.for_linux()
        #user_data.add_commands("yum install -y nginx",
        #                      "chkconfig nginx on", "service nginx start")

        # SSM
        # env = "Preprod"
        # company_param_name = "/Config/" + env + "/CompanyName"
        # company_param = ssm.StringParameter(self, id="Parameter",
        #                                     allowed_pattern='.*',
        #                                     description="The name of the company",
        #                                     string_value="MyAWSomeCompany",
        #                                     tier=ssm.ParameterTier.STANDARD)

        # Instance
        # instance = Instance(self, "Instance",
        #                     instance_type=InstanceType("t3a.nano"),
        #                     machine_image=amzn_linux,
        #                     vpc=vpc,
        #                     key_name="paandrie",
        #                     security_group=sg,
        #                     role=role,
        #                     user_data=user_data
        #                     )
        # Nested stack
        # LambdaCronNestedStack(self, "not:a:stack:name")

        # RDS

        # cluster = rds.DatabaseInstance(self, 'Database',
        #                                engine=rds.DatabaseInstanceEngine.postgres(
        #                                    version=rds.PostgresEngineVersion.VER_12_3),
        #                                instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3,
        #                                                                  ec2.InstanceSize.SMALL),
        #                                master_username='paandrie',
        #                                vpc=vpc)
