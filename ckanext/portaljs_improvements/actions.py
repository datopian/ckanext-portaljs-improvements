import requests
from ckan.plugins.toolkit import chained_action, enqueue_job

def revalidate_vercel(body):
    url = 'https://isr-portaljs.vercel.app/api/revalidate?secret=secret'
    response = requests.post(url, json = body)
    print(response, flush=True)

@chained_action
def package_create(original_action, context, data_dict):
    result = original_action(context, data_dict)
    body = {'dataset': {'name': result['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result


@chained_action
def package_update(original_action, context, data_dict):
    result = original_action(context, data_dict)
    body = {'dataset': {'name': result['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result

@chained_action
def organization_create(original_action, context, data_dict):
    result = original_action(context, data_dict)
    body = {'organization': {'name': result['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result


@chained_action
def organization_update(original_action, context, data_dict):
    result = original_action(context, data_dict)
    body = {'organization': {'name': result['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result

@chained_action
def group_create(original_action, context, data_dict):
    result = original_action(context, data_dict)
    body = {'group': {'name': result['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result


@chained_action
def group_update(original_action, context, data_dict):
    result = original_action(context, data_dict)
    body = {'group': {'name': result['name']}}
    enqueue_job(revalidate_vercel, [body])
    return result