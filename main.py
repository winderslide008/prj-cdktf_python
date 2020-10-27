#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack

from prj_cdktf_python.prj_cdktf_python_stack import PrjCdktfPythonStack


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # define resources here


app = App()
#MyStack(app, "prj-cdktf_python")
PrjCdktfPythonStack(app, "prj-cdktf_python")

app.synth()
