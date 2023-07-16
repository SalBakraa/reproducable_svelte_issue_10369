import type { RequestHandler } from './$types'

export const POST: RequestHandler = async (event) => {
	var body = await event.request.formData()
	body.append('api_key', 'test')

	return await fetch('http://localhost:8000/embed', {
		method: 'POST',
		body: body
	})
}
