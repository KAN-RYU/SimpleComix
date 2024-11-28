<script>
    import { link } from 'svelte-spa-router';
    import { current_dir } from '../lib/store';
</script>

<div>
    <a use:link href="/explorer/" on:click={() => {$current_dir = '/'}}>
        Go
    </a>
</div>