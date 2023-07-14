import requests
from ckan.plugins.toolkit import chained_action, enqueue_job, get_action
from ckan.common import config


def revalidate_vercel(body):
    urls = config.get('ckanext.portaljs_improvements.portal_urls').split(' ')
    secrets = config.get('ckanext.portaljs_improvements.portal_secrets').split(' ')
    for url, secret in zip(urls, secrets):
        print("Sending post request to " + url + " with body " + str(body))
        send_revalidate_request(url, secret, body)

def send_revalidate_request(url, secret, body):
    url = url + "/api/revalidate?secret=" + secret
    response = requests.post(url, json=body)
    print("Response for invalidate request for the following URL " + url + " " + response.text, flush=True)

@chained_action
def package_create(original_action, context, data_dict):
    print("#########\n PACKAGE BEING CREATED \n #############", flush=True)
    result = original_action(context, data_dict)                                                        
    body = {'dataset': {'name': result['name'], 'orgName': result['organization']['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result


@chained_action
def package_update(original_action, context, data_dict):
    print("#########\n PACKAGE BEING UPDATED \n #############", flush=True)
    result = original_action(context, data_dict)                                                               
    body = {'dataset': {'name': result['name'], 'orgName': result['organization']['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result

@chained_action
def package_delete(original_action, context, data_dict):
    print("#########\n PACKAGE BEING DELETED \n #############", flush=True)
    package_info = get_action('package_show')(None, { 'id': data_dict['id'] })
    result = original_action(context, data_dict)
    body = {'dataset': {'name': package_info['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result

@chained_action
def organization_create(original_action, context, data_dict):
    print("#########\n ORGANIZATION BEING CREATED \n #############", flush=True)
    result = original_action(context, data_dict)
    body = {'org': {'name': result['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result

@chained_action
def organization_delete(original_action, context, data_dict):
    print("#########\n ORGANIZATION BEING DELETED \n #############", flush=True)
    org_info = get_action('organization_show')(None, { 'id': data_dict['id'] })
    result = original_action(context, data_dict)
    body = {'organization': {'name': org_info['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result

@chained_action
def organization_update(original_action, context, data_dict):
    print("#########\n ORGANIZATION BEING UPDATED \n #############", flush=True)
    result = original_action(context, data_dict)
    body = {'org': {'name': result['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result


@chained_action
def group_create(original_action, context, data_dict):
    print("#########\n GROUP BEING CREATED \n #############", flush=True)
    result = original_action(context, data_dict)
    body = {'group': {'name': result['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result


@chained_action
def group_update(original_action, context, data_dict):
    print("#########\n GROUP BEING UPDATED \n #############", flush=True)
    result = original_action(context, data_dict)
    body = {'group': {'name': result['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result

@chained_action
def group_delete(original_action, context, data_dict):
    print("#########\n GROUP BEING DELETED \n #############", flush=True)
    group_info = get_action('group_show')(None, { 'id': data_dict['id'] })
    result = original_action(context, data_dict)
    body = {'group': {'name': group_info['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result
