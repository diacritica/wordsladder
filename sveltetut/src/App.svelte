<script>
 let agame = getLadder();

 async function getLadder() {
   const response = await fetch("http://localhost:4000/play?l=4&lang=en&start=dead&end=love");
   const results = await response.json();

   if (response.ok) {
     return results;
   } else {
     throw new Error(todo);
   }
 }
 function handleClick(){
	 agame = getLadder();
 }

</script>


<button on:click={handleClick}>
	Play English Dead to Love
</button>

{#await agame}
	<p>...waiting</p>
{:then results}
<ul>
{#each results as r}
	<li>{r}</li>
{/each}
</ul>
{:catch error}
	<p style="color: red">{error.message}</p>
{/await}

