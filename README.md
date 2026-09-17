# Student Management and Academic Performance System — Jenkins CI/CD

ISWE406P — Agile Development Process & DevOps, Assessment VII, Slot L19+20

One repository, three Jenkins pipeline projects. Each folder is a separate
Jenkins job pointing at this same repo, using the Jenkinsfile in that folder.

Repository: https://github.com/suhaib08/jenkins-project1

## Project 1 — Parameterized Build Pipeline
Folder: `project1-parameterized`

Demonstrates the `parameters` block. Jenkins asks for input *before* the build
starts. A `choice` parameter lets the user pick dev / staging / prod, and the
same Jenkinsfile then behaves differently depending on the value chosen at
trigger time.

Note: the very first run has to be "Build Now" — Jenkins only learns about the
parameters after it has read the Jenkinsfile once. From the second run onward
the sidebar shows "Build with Parameters".

## Project 2 — Archive Build Artifacts Pipeline
Folder: `project2-archive`

Demonstrates `archiveArtifacts`. `app.py` generates `report.txt` containing
student count and average CGPA; the pipeline archives that file so it can be
downloaded from the build page. Each build keeps its own copy, so older builds
still show their original numbers.

## Project 3 — Parallel Stages Pipeline
Folder: `project3-parallel`

Demonstrates the `parallel` block. Frontend and backend checks each sleep 3
seconds. Run sequentially they would take ~6s; in parallel the stage finishes in
~3s, shown by the side-by-side branches in the Jenkins stage view.
