<script lang='ts'>
	import { FileSelector } from "$lib/components/FileSelector";

	async function on_file_selection(file: File) {
		// Create embeddings in the background
		const form_data = new FormData();
		form_data.append('file', file)

		await fetch('/embed', {
			method: 'POST',
			body: form_data,
		})
	}
</script>

<FileSelector {on_file_selection} />
