<script>
    import Router from 'svelte-spa-router';
    import Home from "./routes/Home.svelte";
    import Explorer from "./routes/Explorer.svelte";
    import View from './routes/View.svelte';

    const routes = {
      '/': Home,
      '/explorer': Explorer,
      '/view': View
    }
</script>

<Router {routes}/>