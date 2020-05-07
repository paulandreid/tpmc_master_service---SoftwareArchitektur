node {
    def app
    stage('Notify Discord Build Start') {
        discordSend description: 'Started build for TPMC Master Service', link: env.BUILD_URL, title: JOB_NAME, webhookURL: "${DISCORD_WEBHOOK}", successful: currentBuild.resultIsBetterOrEqualTo('SUCCESS')
    }
    try {
        stage('Clone repository') {
            /* Let's make sure we have the repository cloned to our workspace */

            checkout scm
        }

        stage('Build image') {
            /* This builds the actual image; synonymous to
             * docker build on the command line */

            app = docker.build("tpmc_master_service")
        }

        stage('Test image') {
            docker.image('postgres').withRun('-p ${POSTGRES_PORT}:${POSTGRES_PORT} -e PGPORT=${POSTGRES_PORT} -e POSTGRES_USER=${POSTGRES_USER} -e POSTGRES_NAME=${POSTGRES_DB} -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD}') { c ->
                docker.image('postgres').inside("--link ${c.id}:${POSTGRES_HOST}") {
                    sh "echo 'Started Postgres'"
                }
                app.inside("--link ${c.id}:${POSTGRES_HOST}") {
                    sh 'python /app/manage.py test'
                }
            }
        }

        stage('Push image') {
            /* Finally, we'll push the image with two tags:
             * First, the incremental build number from Jenkins
             * Second, the 'latest' tag.
             * Pushing multiple tags is cheap, as all the layers are reused. */
            docker.withRegistry("${DOCKER_REGISTRY_URL}", 'tpmc_docker_registry_credentials') {
                app.push("${env.BUILD_NUMBER}")
                app.push("latest")
            }
        }

        stage('Notify Discord Build End') {
            discordSend description: 'Build for TPMC Master Service ended', link: env.BUILD_URL, title: JOB_NAME, webhookURL: "${DISCORD_WEBHOOK}", successful: currentBuild.resultIsBetterOrEqualTo('SUCCESS')
        }
    } catch (e) {
        discordSend description: 'Build for TPMC Master Service failed!', link: env.BUILD_URL, title: JOB_NAME, webhookURL: "${DISCORD_WEBHOOK}", successful: false
        /* Since we're catching the exception in order to report on it,
         * we need to re-throw it, to ensure that the build is marked as failed */
        throw e
    }
}
