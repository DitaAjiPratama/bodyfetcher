# BodyFetcher
Python Script for fetch a body request.

## Usage

Let say you want to create a product list API. The usage will looks like this:

    import bodyfetcher
    
    params      = bodyfetcher.body_json()
    response    = api_product.main().product_list(params)
    return json.dumps(response, indent = 2).encode()
