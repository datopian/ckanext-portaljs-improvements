import requests
from ckan.plugins.toolkit import chained_action, enqueue_job
from ckan.common import config


def revalidate_vercel(body):
    url = f"{config.get('ckanext.portaljs_improvements.portal_url')}?secret={config.get('ckanext.portaljs_improvements.portal_secret')}"
    response = requests.post(url, json=body)
    print(response.text, flush=True)


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
