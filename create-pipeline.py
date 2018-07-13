#!/usr/bin/env python
from gomatic import *

configurator = GoCdConfigurator(HostRestClient("localhost:8153", ssl=False))
pipeline = configurator\
	.ensure_pipeline_group("defaultGroup")\
	.ensure_replacement_of_pipeline("MyFirstPipeline")\
	.set_git_url("https://github.com/jfmedeiros1820/library.git")
stage = pipeline.ensure_stage("defaultStage")
job = stage.ensure_job("install")
job.add_task(ExecTask(['npm', 'install']))
job = stage.ensure_job("test")
job.add_task(ExecTask(['bash', '-c', 'CI=true npm test']))
job = stage.ensure_job("build")
job.add_task(ExecTask(['bash', '-c', 'CI=true npm run build']))

configurator.save_updated_config()
