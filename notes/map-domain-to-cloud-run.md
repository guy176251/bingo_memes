# How to map Google Domains domain name to Google Cloud Run project
Below is a post copied verbatim on how to accomplish this. The post was so helpful that I thought I should just add it to the repo in case I forget. Some of the links in the post are borked, but I'm not sure what they were intended to point to, so I just copied the links as they were.

[Link to original post](https://serverfault.com/questions/1053154/how-to-map-google-domains-domain-name-to-google-cloud-run-project-i-cant-make)

---

As mentioned in the comment by @JohnHanley the correct way is to add one mapping for each subdomain (www is a subdomain also) and then proceed to update your DNS with each entrance. To do so you can follow the next steps:

## [Map a custom domain to a service](https://cloud.google.com/run/docs/mapping-custom-domains#dns_update)

> - Open the domain mappings page in the Google Cloud Console: [Domain mappings page](https://console.cloud.google.com/run/domains?_ga=2.237157440.175541525.1614025689-1856969832.1613508180&_gac=1.91115624.1613517072.Cj0KCQiA962BBhCzARIsAIpWEL1-w-Py6R3BcLaxqDZFtTrP1_HxL3BuPKQ5WJTBDcHFm6fYP8vCDxwaAkjwEALw_wcB)
> - In the Domain Mappings page, click Add Mapping.
> - From the dropdown list in the Add Mapping form, select the service you are mapping the custom domain to:
> - Enter the domain name.
> - Click Continue.
> - You need to verify the ownership of a domain before being able to use it, unless you purchased your domain from Google. If you want to map subdomain.example.com, you should verify ownership of example.com. For more information on verifying domain ownership, refer to [Webmaster Central help](https://support.google.com/webmasters/answer/9008080?hl=en)

## [Add your DNS records at your domain registrar](https://cloud.google.com/run/docs/mapping-custom-domains#dns_update)

After you've mapped your service to a custom domain in Cloud Run, you need to update your DNS records at your domain registrar. Cloud Run generates and displays the DNS records you need to enter, you can retrieve the records for each entry [here](https://console.cloud.google.com/run/domains?_ga=2.237140928.175541525.1614025689-1856969832.1613508180&_gac=1.52965850.1613517072.Cj0KCQiA962BBhCzARIsAIpWEL1-w-Py6R3BcLaxqDZFtTrP1_HxL3BuPKQ5WJTBDcHFm6fYP8vCDxwaAkjwEALw_wcB). You must add these records that point to the Cloud Run service at your domain registrar for the mapping to go into effect. I want to emphasize the next part on the [documentation](https://cloud.google.com/run/docs/mapping-custom-domains#dns_update) as it mentions the www subdomain:

When you add each of the above DNS records to the account at the DNS provider:

> - Select the type returned in the DNS record in the previous step: A, or AAAA, or CNAME.
> - **Use the name www to map to www.example.com**

And that's the right way to perform the domain mapping for the `www` subdomain
