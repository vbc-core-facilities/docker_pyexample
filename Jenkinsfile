def towerJobs = [
  master: [jobName:"App Conv Docker Image", extraVars: "app_generic_image_tag: master"],
]

buildDockerImage([
  imageName: "pyexample",
  pushRegistry: "docker.artifactory.imp.ac.at",
  pushRegistryNamespace: "hpctraining",
  pushBranches: ["master"],
  tower: towerJobs
])