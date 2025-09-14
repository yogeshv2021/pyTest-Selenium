import os,subprocess

if __name__=="__main__":
    try:
        runcomand="pytest -s tests/ --html=report.html --self-contained-html"
        result = subprocess.Popen(runcomand,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        if result.returncode is None:
            result.communicate()
        else:
            print("not started")
    except Exception as error:
        print("Error occures %s" %error)

