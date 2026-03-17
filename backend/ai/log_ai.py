def analyze_log(log):

    issues = []

    log = log.lower()

    if "error" in log:

        issues.append("error detected")

    if "timeout" in log:

        issues.append("driver timeout possible")

    if "panic" in log:

        issues.append("kernel panic pattern detected")

    return {

        "issues": issues
    }
