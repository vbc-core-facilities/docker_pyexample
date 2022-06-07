// Based on "webdock"'s Jenkinsfile
// hope it goes to local-docker/vbcf/training/pyexample
def towerJobs = [
  master: [jobName:"App Training Website", extraVars: "app_generic_image_tag: master"],
]

buildDockerImage([
    imageName: "pyexample",
    pushRegistryNamespace: "vbcf/training",
    pushBranches: ['master'],
    tower: towerJobs
])

// ----------

// This worked, see commit cfb3f2e and tag "docker_hpctraining"
// image goes to artifactory.imp.ac.at/docker/hpctraining/pyexample
// buildDockerImage([
//   imageName: 'pyexample',
//   pushRegistry: 'docker.artifactory.imp.ac.at',
//   pushRegistryNamespace: 'hpctraining',
//   pushBranches: ['master']
// ])
