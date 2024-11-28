<script>
    import { link } from 'svelte-spa-router';
    import { current_dir } from '../lib/store';
    let files = {};
    function get_file_list(_dir) {
        fetch("http://127.0.0.1:8000/list"+_dir).then((response) => {
            response.json().then((json) => {
                files = json;
                $current_dir = _dir
            });
        });
    }

    get_file_list($current_dir);
</script>

<div>
    <button on:click={() => get_file_list("/")}>
        Root
    </button>
    <a use:link href="/view/">
        view
    </a>
</div>

<ul>
    {#each files.file_list as file}
        <li>{file}</li>
    {/each}
</ul>

<ul>
    {#each files.directory_list as directory}
        <li><button on:click={() => get_file_list($current_dir+directory+"/")}>{directory}</button></li>
    {/each}
</ul>
