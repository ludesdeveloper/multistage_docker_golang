podTemplate(yaml: """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: docker
    image: docker:1.11
    command: ['sleep', '99d']
    tty: true
    volumeMounts:
    - name: dockersock
      mountPath: /var/run/docker.sock
  volumes:
  - name: dockersock
    hostPath:
      path: /var/run/docker.sock
"""
  ) {

  def image = "app"
  node(POD_LABEL) {
    stage('Build Docker image') {
      checkout scm 
      container('docker') {
        sh "docker build -t ${image} ."
        sh "docker images -a"
        try {
          sh "docker run --name app -d -p 5000:5000 ${image}"
        } catch (err) {
          echo "Failed: ${err}"
          sh "docker stop ${image}"
          sh "docker rm ${image}"
        }
        sh "docker ps -a"
        sh "docker stop ${image}"
        sh "docker rm ${image}"
        sh "docker rmi ${image}"
      }
    }
  }
}
