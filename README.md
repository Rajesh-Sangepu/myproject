1. Create a repo with some code in main branch
2. Creare another branch with some secret exposed in dev branch
3. Write a github action which triggers upon PR raise event
4. Run secret scan using any tool (e.g trivy, trufflehog)on the dev branch to check if developer is adding any faulty code.
5. If any failure is there then fail the github action.
