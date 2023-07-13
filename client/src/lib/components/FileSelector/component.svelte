<script lang='ts'>
	export let on_file_selection: (file: File) => void;

	async function file_selection_handler(this: HTMLInputElement) {
		const file = this?.files?.[0]
		if (!file) {
			return
		}
		on_file_selection?.(file)
	}
</script>

<label class='file-selector'>
	<div class='upload-label'>
		<input type='file' on:change|preventDefault={file_selection_handler} accept='audio/wav' style='display: none'>
		<div class='upload-button'>
			Search
		</div>
		<div class='upload-filename'>
			filename
		</div>
	</div>
</label>


<style lang='scss'>
.file-selector {
	height: 2.5rem;
	width: 100%;
	max-width: 100%;
	cursor: pointer;

	.upload-label {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-wrap: nowrap;
		gap: 0;

		width: 90%;
		max-width: 90%;
		margin: auto;

		.upload-button {
			max-width: 20%;

			height: 2.5rem;
			padding: 0rem .5rem;

			border: .075rem solid #ddd;
			border-radius: 6px 0 0 6px;
			border-right-width: 0;

			line-height: 2rem;
			color: #555;
			background-color: #eee;
		}

		.upload-filename {
			width: 80%;
			max-width: 80%;

			height: 2.5rem;
			padding: 0px 10px;

			border: .075rem solid #ddd;
			border-radius: 0 6px 6px 0;
			box-shadow: inset 0 .2rem .4rem rgba(0,0,0,.05);

			line-height: 2rem;
			text-align: left;
			color: #555;
			background-color: #fff;

			-webkit-user-select: none;
			-moz-user-select: none;
			-ms-user-select: none;
			user-select: none;

			overflow: hidden;
			white-space: nowrap;
			text-overflow: ellipsis;
		}
	}
}
</style>
