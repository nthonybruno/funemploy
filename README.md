# FunEmploy
A smarter way to job hunt. (In the works, project started 7/6/2022)

## Elevator Pitch
FunEmploy puts the fun back into the job search process by taking the work out of it. Getting a job has become a full time job. This project will automate the job search process by bringing relevant listings directly to the user across various job-posting platforms. It addresses the problem the average job-seeker faces of tediously sifting through job postings across multiple sites to find relevant listings that match the seeker's interests, experience and salary expectations. Better yet, FunEmploy offers email and SMS notifications on new job postings across sites. FunEmploy brings relevant jobs right to the user, and with the notification system they can be one of the first to apply.


## Design Premise
Site connectors fetch semi-relevant job postings from numerous job sites based on user descretion (Experience Level, Title, Location, etc.) -> Filter Algorithm applies second layer of filtering so user only sees hyper relevant listings -> Notification system alerts user of relevant listings (Twilio SMS, SMTP Email) -> Automated background scan regularly checks for new listings, alerts user if/when -> Front End (FunEmploy.net)

## Up Next
1. Begin building FunEmploy core app functionality
   1. [Startup.jobs](https://startup.jobs/) connector (Web Scraping w/ Python)
   2. [LinkedIn](https://www.linkedin.com/jobs) connector (API)
   3. Google Jobs connector (API) 
   4. [Indeed](https://www.indeed.com/) connector (API)
   5. [builtin](https://builtin.com/jobs) connector (Web Scraping w/ Python)
   6. [Glassdoor](https://www.glassdoor.com/index.htm) connector (Web Scraping w/ Python)
   7. [Levels](https://www.levels.fyi/still-hiring/) connector (Web Scraping w/ Python)
 2. Much more, TBD

## Completion Log
**June 6th, 2022**
- Registered [FunEmploy.net](www.funemploy.net) with GoDaddy
- Created this GitHub repo
- Built custom HTML splash page to park on domain for time being

**June 7th, 2022**
- Created funemploy.net splash page [repo](https://github.com/nthonybruno/funemploy-splash-page)
- Pushed custom HTML splash page contents to the repo and set up Pages for it
- Added GitHub Pages DNS records to funemploy.net on GoDaddy
- Set up CloudFlare account for free SSL certificating
- Transfered GoDaddy nameservers to CloudFlare nameservers, website now uses HTTPS
- Updated HTML splash page to be responsive and include favicon, site now functional and live
- Added GitHub link to splash page, logo on the page is a link. Just tap the screen.
