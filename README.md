# ckanext-portaljs-improvements

This extension has one my purpose, to allow the use of On demand Incremental Static Regeneration(On demand ISR) on Portal.JS websites.
NextJS has three ways of fetching data, client fetching, ServerSideRendering and StaticSite Generation(SSG).

- Client fetching allows us to send the skeleton of the page quickly, and then populate it with information using javascript, that has a lot of problems, the SEO get considerably affected, because the google crawlers can't index the pages easly, there is also the problem of layout shifting, and also the browsers can't cache the pages easly
- Serverside rendering, has the advantages of SEO, no layout shifting and a easier time for caching, the problem is that we need to wait for all tha data to be fetched to show something on the screen to the user, depending on the page that could mean a lot of time
- StaticSite Generation is a little bit different, we build the pages ahead of time, fetch all the data, inject that data into the html, and once the user requests it we just send everything already filled, this makes the page loads super fast and already with all the information needed, the SEO is great, the caching is great, there is no layout shift and perhaps most important, this allows us to use the `<Link>` tag to its fullest potential, when you have a static page that is linked using a `<Link>` tag, Next prefetches the html, for instance, if you have a list of 5 dataset pages, as soon the page loads, Next will use the iddle time to fetch everyone of those 5 pages on the background, this basically means app like speed when changing from one page to the next.
  But if StaticSite Generation is so awesome, why do we use the other two tactics most of the time? Thats because in SSG the pages are only built once when the project is deploy the project, so if someone changes an information after the deploy the only way to update that is by redeploying everything. There is a way in Next to schedule rebuilds, called Incremental Static Regeneration, for instance i can say "rebuild every page with X url every 60 seconds" but then there are two problems. Firstly you are making unecessary requests to the data source(ckan api for instance) and secondly there is still a delay between the data being updated and that being reflected on the page.

On demand ISR Solves the problems with StaticSite Generation and with normal ISR, the idea behind On demand ISR is that if there was a way for the data source to inform the frontend that some data has been updated, then the frontend would be able to change the pages that use that data and only those pages, this is possible because even tough we say NextJS is a frontend solution, thats kind of misleading, because there is still a server process running continuously, and that server can be interacted with. Previously the Ckan instance didn't know about the existance of a PortalJS website fetching data from it, this is reflected by the fact that i don't need authorization to fetch data from a Ckan instance, what this is extension does is basically make the Ckan backend aware of the existance of a PortalJS website, so, its quite simple, all we do is make sure that after every update/create and equivalent process, we make sure to update the corresponding pages on the backend, basically building a cache of sorts, this also has the advantage of saving resources on the backend, decreasing the amount of times that it has to fetch data from the database for instance.

## Requirements

**TODO:** For example, you might want to mention here which versions of CKAN this
extension works with.

If your extension works across different versions you can add the following table:

Compatibility with core CKAN versions:

| CKAN version    | Compatible? |
| --------------- | ----------- |
| 2.6 and earlier | not tested  |
| 2.7             | not tested  |
| 2.8             | not tested  |
| 2.9             | yes         |

## Installation

To install ckanext-portaljs-improvements:

1. Activate your CKAN virtual environment, for example:

   . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

   git clone https://github.com/datopian/ckanext-portaljs-improvements.git
   cd ckanext-portaljs-improvements
   pip install -e .
   pip install -r requirements.txt

3. Add `portaljs-improvements` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

   ```
    sudo service apache2 reload
   ```

## Config settings

None at present, but there will be

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
