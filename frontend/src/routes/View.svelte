<script>
    import { current_dir } from "../lib/store";
    let files = {};
    function get_file_list(_dir) {
        fetch("http://127.0.0.1:8000/list" + _dir).then((response) => {
            response.json().then((json) => {
                files = json;
            });
        });
    }

    get_file_list($current_dir);
</script>

<div class="viewer">
    {#each files.file_list as file}
        <img
            src={"http://127.0.0.1:8000/file" + $current_dir + file}
            alt={file}
        />
    {/each}
</div>

<style>
    .viewer {
        width: 100%;
    }

    img {
        width: 100%;
    }
</style>