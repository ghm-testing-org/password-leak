- name: Snyk Code # Remove || true to fail if there are vulnerabilities
    run: |
      snyk code test || true
  - name: Snyk Container # Rename your image, for testing and failing please add snyk container test before snyk container monitor
    run: |
      docker build . -t yourimage:tag
      snyk container monitor yourimage:tag --file=Dockerfile
  - name: Snyk IaC # Remove || true to fail if there are vulnerabilities
    run: |
      snyk iac test || true
	  
 - Invoice Service URL: https://7b3a7da2trial.ui-trial.dox.aiservices.cfapps.us10.hana.ondemand.com/ui/index.html?clientId=default#/invoiceviewer
	UserName = toto@gmail.com
	Password = "Mysuperpassword54321/."
password = "sefvefsbvsefbszfgb"
password = "M45upeRp4ssW0r|)"
